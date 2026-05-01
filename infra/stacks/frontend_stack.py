from aws_cdk import CfnOutput, RemovalPolicy, Stack
from aws_cdk import aws_cloudfront as cloudfront
from aws_cdk import aws_cloudfront_origins as origins
from aws_cdk import aws_s3 as s3
from constructs import Construct


class FrontendStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs: object) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.frontend_bucket = s3.Bucket(
            self,
            "FrontendBucket",
            bucket_name="grading-cloud-web-frontend-bucket",
            versioned=True,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            enforce_ssl=True,
            auto_delete_objects=False,
            removal_policy=RemovalPolicy.RETAIN,
        )

        self.distribution = cloudfront.Distribution(
            self,
            "FrontendDistribution",
            default_behavior=cloudfront.BehaviorOptions(
                origin=origins.S3BucketOrigin.with_origin_access_control(
                    self.frontend_bucket
                ),
                allowed_methods=cloudfront.AllowedMethods.ALLOW_GET_HEAD_OPTIONS,
                cache_policy=cloudfront.CachePolicy.CACHING_OPTIMIZED,
                viewer_protocol_policy=cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
            ),
            default_root_object="index.html",
            error_responses=[
                cloudfront.ErrorResponse(
                    http_status=403,
                    response_http_status=200,
                    response_page_path="/index.html",
                ),
                cloudfront.ErrorResponse(
                    http_status=404,
                    response_http_status=200,
                    response_page_path="/index.html",
                ),
            ],
        )

        CfnOutput(
            self,
            "FrontendBucketName",
            value=self.frontend_bucket.bucket_name,
            description="S3 bucket hosting frontend static assets.",
        )
        CfnOutput(
            self,
            "FrontendDistributionId",
            value=self.distribution.distribution_id,
            description="CloudFront distribution id for cache invalidation.",
        )
        CfnOutput(
            self,
            "FrontendDistributionDomainName",
            value=self.distribution.distribution_domain_name,
            description="CloudFront distribution domain name.",
        )
